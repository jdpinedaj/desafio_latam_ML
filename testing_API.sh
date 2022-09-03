

# script.lua
# HTTP POST script which demonstrates setting the HTTP method, body, and adding a header
wrk.method = "POST"
wrk.body   = '{"OPERA": "Grupo LATAM", "MES": 1, "TIPOVUELO": "I"}'
wrk.headers["Content-Type"] = "application/json"

# Output
# Implementing wrk using 50.000 requests and 45 seconds to http://localhost:8000
wrk -c50000 -d45s http://localhost:8000/

# Implementing wrk using 50.000 requests and 45 seconds to prediction, using a script.lua
wrk -c50000 -d45s -s ./post.lua http://localhost:8000/predict

