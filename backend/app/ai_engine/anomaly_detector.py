import pandas as pd

from sklearn.ensemble import IsolationForest


class AnomalyDetector:

    @staticmethod
    def detect(metrics):

        if len(metrics) < 10:
            return []

        df = pd.DataFrame(metrics)

        model = IsolationForest(
            contamination=0.1,
            random_state=42
        )

        predictions = model.fit_predict(df)

        anomalies = []

        for idx, prediction in enumerate(predictions):

            if prediction == -1:

                anomalies.append({
                    "index": idx,
                    "cpu_usage": df.iloc[idx]["cpu_usage"],
                    "memory_usage": df.iloc[idx]["memory_usage"],
                    "disk_usage": df.iloc[idx]["disk_usage"]
                })

        return anomalies