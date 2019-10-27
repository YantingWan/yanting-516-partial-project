Yanting's own test and experiment for 516 final project.

Some handy commands to run the program:
1. curl -X POST "http://localhost:8000/kmeans/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@model.csv;type=text/csv"
2. curl -X POST "http://localhost:8000/kmeans/fit" -H "accept: text/csv" -H "Content-Type: application/json" -d "{\"job_id\":0,\"model_params\":{\"n_clusters\":3}}"
3. curl -X POST "http://localhost:8000/kmeans/predict" -H "accept: text/csv" -H "Content-Type: multipart/form-data" -F "job_id=0" -F "file=@predict.csv;type=text/csv"