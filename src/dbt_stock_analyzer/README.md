Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

### Docker:
To build the docker image
```
docker build -t dbt-dev:latest .
```

To run the docker container
```
docker run --name dbt -p 127.0.0.1:8000:8000 dbt-dev:latest
```

To connect to the container via interactive terminal
```
docker exec -it dbt bash
```