FROM python:3.10
RUN mkdir spybot_sb
WORKDIR /spybot_sb
COPY requirements.txt .
RUN  pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh