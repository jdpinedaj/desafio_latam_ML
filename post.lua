-- HTTP POST script which demonstrates setting the HTTP method, body, and adding a header
wrk.method = "POST"
wrk.body   = "OPERA=Avianca&MES=1&TIPOVUELO-I"
wrk.headers["Content-Type"] = "application/x-www-form-urlencoded"