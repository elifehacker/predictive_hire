# predictive_hire
## Answer to question
(1) Regarding the mode building, how would you increase the accuracy of the model. 
1. add more data
2. figure out the actual outcome of -1 data
3. find the most critical feature of each job title and build separate model
4. use multiple algorithms such as the work done in some_ml_work.ipynb
5. fine tune each algorithm with different parameter values

(2) Regarding the docker deployment, what are the services you would consider if you are to deploy the docker as an actual web service in the cloud, e.g., AWS. 
VPC, ECS, EFS, and maybe terraform to allow IaC

(3) How would you reduce the response time and increase throughput of the deployed service in the cloud?
1. deploy in mutiple regions to reduce latency
2. make service auto scalable to increase throughput
3. use monitoring tool such as datadog, kibana, grafana, prometheus etc to find bottleneck and resolve corresondingly.

## original task

Task
1: Build a model in Python to predict “selected” based on both multiple-choice answers, and text responses.
We will not care about what you get for performance metrics such F1 score etc, so don’t spend time trying to improve on those (given the random nature of the data, those values will not mean much).  

2: Build a Restful API in the local machine with the input of multiple-choice answer and text response, and the output of a likelihood of being selected
You might design the exact format of the input and output,
We will not care about the performance of this RESTful API such as response speed, throughput.

3: Dockerise the Restful API. When the docker application starts, it will start a local server with the RESTful API.
The whole implementation (task 1-3) can be simple (~5hrs effort)

4: Write a short description of the methodology and key results you would consider in a complete solution. For example: 
(1) Regarding the mode building, how would you increase the accuracy of the model. 
(2) Regarding the docker deployment, what are the services you would consider if you are to deploy the docker as an actual web service in the cloud, e.g., AWS. 
(3) How would you reduce the response time and increase throughput of the deployed service in the cloud?
