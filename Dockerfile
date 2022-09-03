# Some container that is already suitable for unicover
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR '/app/app'
COPY ./Pipfile ./
COPY ./Pipfile.lock ./
# install dependencies, 
# we could probably find an image including this
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
# RUN pipenv lock -r > requirements.txt
# RUN pip install -r requirements.txt
COPY ./test_main.py ./
COPY ./main.py ./
COPY ./data ./data
COPY ./models ./models
# do tests, usually better to do befor building container, e.g. travis, circelci
RUN python test_main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]