# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:08:31 2021

@author: BAASHITH
"""

from flask import Flask,redirect,url_for,render_template,request
import pickle
import pandas as pd
import sklearn




app= Flask (__name__)
loaded_modell = pickle.load(open("score.pkl","rb"))

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
            
def predict():
    if request.method == 'POST':
        bat_team = request.form['bat_team']
        if (bat_team == 'Chennai Super Kings') :
            bat_team_ChennaiSuperKings = 1
            bat_team_DelhiDaredevils =0
            bat_team_KingsXIPunjab =0
            bat_team_KolkataKnightRiders =0
            bat_team_MumbaiIndians =0
            bat_team_RajasthanRoyals =0
            bat_team_RoyalChallengersBangalore =0
            bat_team_SunrisersHyderabad =0
        elif (bat_team == 'Delhi Capitals') :
            bat_team_ChennaiSuperKings = 0
            bat_team_DelhiDaredevils=1
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=0
        elif (bat_team == 'Punjab Kings') :
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=1
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=0
        elif (bat_team == 'Kolkatha knight Kiders') :
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=1
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=0
        elif (bat_team == 'Mumbai Indians') :
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=1
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=0
        elif (bat_team == 'Rajasthan Royals') :
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=1
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=0
        elif (bat_team == 'Royal challangers Banglore') :
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=1
            bat_team_SunrisersHyderabad=0
        else :
            
            bat_team_ChennaiSuperKings=0
            bat_team_DelhiDaredevils=0
            bat_team_KingsXIPunjab=0
            bat_team_KolkataKnightRiders=0
            bat_team_MumbaiIndians=0
            bat_team_RajasthanRoyals=0
            bat_team_RoyalChallengersBangalore=0
            bat_team_SunrisersHyderabad=1
        
        bowl_team = request.form['bowl_team']
        if (bowl_team == 'Chennai Super Kings') :
            bowl_team_ChennaiSuperKings=1
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Delhi Capitals') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=1
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Punjab Kings') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=1
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Kolkatha knight Kiders') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=1
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Mumbai Indians') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=1
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Rajasthan Royals') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=1
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=0
        elif (bowl_team == 'Royal challangers Banglore') :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=1
            bowl_team_SunrisersHyderabad=0
        else :
            bowl_team_ChennaiSuperKings=0
            bowl_team_DelhiDaredevils=0
            bowl_team_KingsXIPunjab=0
            bowl_team_KolkataKnightRiders=0
            bowl_team_MumbaiIndians=0
            bowl_team_RajasthanRoyals=0
            bowl_team_RoyalChallengersBangalore=0
            bowl_team_SunrisersHyderabad=1
            
        venue = request.form['venue']
        if (venue ==  'Rajasekhara Reddy vizag') :
            rajasekharaReddyvizag = 1
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Dubai International Cricket Stadium'  ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 1
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Eden Gardens'  ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 1
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Feroz Shah Kotla' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 1
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'M Chinnaswamy Stadium' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=1
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Chidambaram Stadium Chepauk' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=1
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'IS Bindra Stadium Mohali' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=1
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Rajiv Gandhi International Stadium Uppal'  ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=1
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Sawai Mansingh Stadium' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =1
            sharjah =0
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Sharjah Cricket Stadium' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =1
            sheikhZayed = 0
            wankhede =0
        elif (venue == 'Sheikh Zayed Stadium' ):
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 1
            wankhede =0
        else :
            rajasekharaReddyvizag = 0
            dubaiStadium = 0
            edenGardens = 0
            ferozShahKotla = 0
            chinnaswamyStadium=0
            chepauk=0
            isBindra=0
            rajivGandhiUppal=0
            sawaiMansingh =0
            sharjah =0
            sheikhZayed = 0
            wankhede =1
            
            
        
            
        runs=int(request.form['runs'])
        
        wickets=int(request.form['wickets'])
        
        overs=float(request.form['overs'])
        
        runs_last_5=int(request.form['runs_last_5'])
        
        wickets_last_5=int(request.form['wickets_last_5'])
        if(wickets_last_5 < wickets and bat_team != bowl_team and wickets<=9 and overs<=19.5 ):
            final_prediction=loaded_modell.predict([[bat_team_ChennaiSuperKings, bat_team_DelhiDaredevils,
            bat_team_KingsXIPunjab, bat_team_KolkataKnightRiders,
            bat_team_MumbaiIndians, bat_team_RajasthanRoyals,
            bat_team_RoyalChallengersBangalore, bat_team_SunrisersHyderabad,
            bowl_team_ChennaiSuperKings, bowl_team_DelhiDaredevils,
            bowl_team_KingsXIPunjab, bowl_team_KolkataKnightRiders,
            bowl_team_MumbaiIndians, bowl_team_RajasthanRoyals,
            bowl_team_RoyalChallengersBangalore,
            bowl_team_SunrisersHyderabad,rajasekharaReddyvizag,dubaiStadium,edenGardens ,ferozShahKotla,
            chinnaswamyStadium,chepauk,isBindra,rajivGandhiUppal,sawaiMansingh,sharjah,sheikhZayed,
            wankhede,runs, wickets, overs, runs_last_5, wickets_last_5]])
    
            output=round(final_prediction[0],0)
            from_score= output - 6
            to_score= output + 6
            if (output>0) :
                return render_template('index.html',prediction_texts="predicted 1st innings score : {} to {}".format(from_score,to_score))
            else :
                return render_template('index.html',prediction_texts="!!Given invalid input!!")
        else :
                return render_template('index.html',prediction_texts="Given invalid input!!")
            
    else:
        return render_template('index.html')
        
        
            
            
    
            
if __name__=='__main__':
    app.run()