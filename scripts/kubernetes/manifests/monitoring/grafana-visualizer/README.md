## Installation

We will use Helm to deploy Grafana Dashboard on to our K8s cluster. You need to have both Helm server and client installed on your machine. Please move to helm folder for applying required configurations to our k8s cluster.

We have defined Prometheus as data source for Grafana in `configMap.yaml` file. The file `getDataSources.yaml` overrides the defaults provided by Helm and uses our `configMap.yaml` for data source.

```
$ helm install stable/grafana \
    -f monitoring/grafana/values.yml \
    --namespace bassa-monitoring \ 
    --name grafana
```

Once all the required scripts are applied, we shall retrieve the password for Grafana by using the below command
```
$ kubectl get secret \
    --namespace bassa-monitoring \
    grafana \
    -o jsonpath="{.data.admin-password}" \
    | base64 --decode ; echo
```
Let's port-forward to access Grafana on our machine.

```
$ export POD_NAME=$(kubectl get pods --namespace bassa-monitoring -l "app=grafana,release=grafana" -o jsonpath="{.items[0].metadata.name}")
$ kubectl --namespace bassa-monitoring port-forward $POD_NAME 3000
```
Now finally lets add a dashboard to visualize our metrics

Use `1860` as dashboard ID anyways you may use any other dashboard ID.
Select the data source on dashboard and you should see the metrics