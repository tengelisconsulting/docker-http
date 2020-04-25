local cjson = require "cjson"
local hmac = require "resty.openssl.hmac"
local shell = require "resty.shell"

local log = require "lua/log"

local HOOK_KEY_S = os.getenv("HOOK_KEY")
local HOOK_KEY = ngx.decode_base64(HOOK_KEY_S)

                -- local timeout = 1000
                -- local max_size = 4096
                -- shell.run([[/app/scripts/load_latest_galleri_webapp.sh]])

local function handle_build_success(repo_name)
   ngx.req.read_body()
   local data = cjson.decode(ngx.req.get_body_data())
   local digest_algo = data.digest_algo
   local req_payload = data.payload
   local req_payload_sig_b64 = data.payload_signed_b64
   local payload_hmac = hmac.new(HOOK_KEY, "sha256")
   payload_hmac:update(req_payload)
   local calced_sig_bytes = payload_hmac:final()
   local calced_sig_b64 = ngx.encode_base64(calced_sig_bytes)
   if calced_sig_b64 ~= req_payload_sig_b64 then
      log.info("unauthorized access")
      ngx.exit(403)
      return
   end
   ngx.say(cjson.encode({
                 success = repo_name,
   }))
end

local M = {}
M.handle_build_success = handle_build_success
return M


-- # shell.run([[/app/scripts/load_latest_galleri_webapp.sh]], "", timeout, max_size)
