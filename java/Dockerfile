FROM openjdk:26-ea-jdk-slim-trixie

WORKDIR /app

COPY /src/Main.java /app/Main.java

RUN javac Main.java

CMD ["java", "Main"]
