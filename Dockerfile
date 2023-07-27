FROM python:3.9

# Set envs for no bytecode write and immediate output when python script runs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code


# Copy everything into docker /code
COPY . /code


# Install requirements
RUN python3.9 -m pip install -r requirements.txt

EXPOSE 3000

#RUN
CMD python ./wsgi.py
