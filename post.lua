-- HTTP POST script which demonstrates setting the HTTP method, body, and adding a header
wrk.method = "POST"
wrk.body   = '{"OPERA": "Grupo LATAM", "MES": 1, "TIPOVUELO": "I"}'
wrk.headers["Content-Type"] = "application/json"