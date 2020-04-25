FROM busybox

RUN ls

ENTRYPOINT [ "/bin/sh" ]
