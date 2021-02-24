FROM fedora

WORKDIR /ctf
RUN dnf install -y coreutils bash python3 python3-pip
RUN pip3 install django
COPY . ./
#COPY ./** ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD "/bin/bash"
