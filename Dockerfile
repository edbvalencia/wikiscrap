FROM python:3.8

RUN pip install pipenv

ENV PIPENV_VENV_IN_PROJECT=1
  
WORKDIR /app

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t robbyrussell \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-syntax-highlighting \
    -p https://github.com/zsh-users/zsh-completions \
    -p https://github.com/rupa/z/

EXPOSE 8000
 
CMD [ "/bin/zsh"]
