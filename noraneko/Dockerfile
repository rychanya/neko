# FROM node AS build-spa
# WORKDIR /app
# COPY koneko/package*.json ./
# RUN npm install
# COPY koneko/ .
# RUN npm run build

FROM python
EXPOSE 80
# COPY --from=build-spa /app/dist /spa
COPY pyproject.toml pdm.lock README.md /temp/app/
COPY src/ /temp/app/src
RUN pip install /temp/app
ENV APP_SIGNAL_HANDLER=1
CMD ["noraneko-cli"]