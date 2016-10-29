FROM centos:7
MAINTAINER Visgence Inc <info@visgence.com>

RUN systemctl mask firewalld.service

RUN yum install -y epel-release

RUN yum install -y screen && yum clean all
RUN yum install -y git && yum clean all

RUN yum install -y python-setuptools && yum clean all
RUN easy_install pip

RUN pip install ipython
RUN pip install requests
RUN yum install -y net-snmp-python

RUN yum install -y postgresql && yum clean all

RUN pip install django==1.8
#RUN pip install django-localflavor
RUN pip install South

RUN yum install -y make automake gcc gcc-c++ && yum clean all
RUN yum install -y python-devel && yum clean all
RUN yum install -y postgresql-devel && yum clean all
RUN pip install psycopg2

RUN adduser electroinv

USER electroinv
WORKDIR /home/electroinv/electroinv/docker/app

USER root
ADD gen_pgpass.sh /home/electroinv
RUN chmod u+x /home/electroinv/gen_pgpass.sh
RUN chown electroinv:electroinv /home/electroinv/gen_pgpass.sh
USER electroinv

RUN echo "~/gen_pgpass.sh > ~/.pgpass" >> ~/.bashrc
RUN echo "chmod 0600 ~/.pgpass" >> ~/.bashrc
RUN echo "cd /home/electroinv/" >> ~/.bashrc
RUN echo "export DOCKER=true" >> ~/.bashrc

VOLUME ["/home/electroinv/electroinv"]

expose 8000

USER electroinv
CMD ["/bin/bash"]
