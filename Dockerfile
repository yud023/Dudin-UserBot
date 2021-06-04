# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# REBELLIONS-UserBot
#
RUN git clone -b REBELLIONS-UserBot https://github.com/yud023/REBELLIONS-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/yud023/REBELLIONS-UserBot/REBELLIONS-UserBot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
