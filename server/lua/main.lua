local cjson = require "cjson"
local hmac = require "resty.openssl.hmac"

local log = require "lua/log"

local LOCAL_HOOK_PORT = tonumber(os.getenv("LOCAL_HOOK_PORT"))
local HOOK_KEY_S = os.getenv("HOOK_KEY")
local HOOK_KEY = ngx.decode_base64(HOOK_KEY_S)


local function unauthorized(msg)
   ngx.status = 401
   log.err(msg)
   ngx.say(cjson.encode(msg))
   ngx.exit(401)
end

local function verify(data)
   local digest_algo = data.digest_algo
   local req_payload = data.payload
   local req_payload_sig_b64 = data.payload_signed_b64
   local payload_hmac = hmac.new(HOOK_KEY, "sha256")
   payload_hmac:update(req_payload)
   local calced_sig_bytes = payload_hmac:final()
   local calced_sig_b64 = ngx.encode_base64(calced_sig_bytes)
   if calced_sig_b64 ~= req_payload_sig_b64 then
      unauthorized("bad signature")
      return
   end
   local payload_data = cjson.decode(req_payload)
   local req_ts = payload_data.req_ts
   if math.abs(os.time() - req_ts) > 60 then
      unauthorized(string.format("bad timestamp - %s", req_ts))
      return
   end
end

local M = {}

function M.main()
   ngx.req.read_body()
   local body = ngx.req.get_body_data()
   if not body then
      unauthorized("no body")
   end
   local data = cjson.decode(body)
   verify(data)
   local socket = ngx.socket.tcp()
   local ok, err = socket:connect("127.0.0.1", LOCAL_HOOK_PORT)
   local ok, err = socket:send(ngx.var.request_uri)
   socket:close()
end

return M
