
import pandas as pd
class stop_link_model():
    """
    Simple class contains two linear regression models - one for dwell time and one for travel time.

Should be able to model the time taken to get between two stops
    """
    
    def __init__(self,from_stop,to_stop,data,clf='Linear'):
        if clf not in ('neural','forest'):
            from sklearn.linear_model import LinearRegression
            self.clf = LinearRegression(fit_intercept=True)
        elif clf=='neural':
            from sklearn.neural_network import MLPRegressor
            self.clf = MLPRegressor(hidden_layer_sizes=(100,), alpha=0.0001)

        self.from_stop = from_stop
        self.to_stop = to_stop
        self.data = data
        self.buildDwellTimeModel()
        self.buildTravelModel()
        del(self.data)
    def buildDwellTimeModel(self):
        target = 'dwelltime'
        features = ['actualtime_arr_from','dayofweek','month','weekend']
        self.dwell_regr = self.clf.fit(self.data[features],self.data[target])
    def buildTravelModel(self):
        target= 'traveltime'
        features = ['actualtime_dep_from','dayofweek','month','weekend']
        self.travel_regr=self.clf.fit(self.data[features],self.data[target])
    
    def get_time_to_next_stop(self, arrival_time, dayofweek,month,weekend):
        index1 = ['actualtime_arr_from','dayofweek','month','weekend']
        index2 = ['actualtime_dep_from','dayofweek','month','weekend']
        row = pd.DataFrame([[arrival_time,dayofweek,month,weekend]],index=index1)
        leavetime = self.dwell_regr.predict(row)[0]
        row2 = pd.DataFrame([[leavetime,dayofweek,month,weekend]],index=index2)
        arrival_time = self.travel_regr.predict(row2)[0]
        return arrival_time
        
