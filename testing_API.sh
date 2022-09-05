

# post.lua
# HTTP POST script setting the HTTP method, body, and adding a header
wrk.method = "POST"
wrk.body   = '{"OPERA": "Grupo LATAM", "MES": 1, "TIPOVUELO": "I"}'
wrk.headers["Content-Type"] = "application/json"

# Output
# Implementando wrk, usando 50.000 requests y 45 segundos en http://localhost:8000
wrk -c50000 -d45s http://localhost:8000/

# Implementando wrk, usando 50.000 requests y 45 segundos en la funcion de predicción, usando el sript en `post.lua`
wrk -c50000 -d45s -s ./post.lua http://localhost:8000/predict

