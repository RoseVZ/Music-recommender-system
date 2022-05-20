from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import h11
from sklearn.metrics.pairwise import cosine_similarity  
import pickle
import numpy as np
import pandas as pd
from flask.views import MethodView
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
import jsonify
app = Flask(__name__)
api=Api(app)

parser = reqparse.RequestParser()
parser.add_argument('query')

dataset=pd.read_csv('datacomp2 2.csv')


count = CountVectorizer(stop_words=None)

def soup(x):
    return ' '.join(x['Genres']) + ' ' + x['Artist']
dataset['soup'] = dataset.apply(soup, axis=1)
matrix=count.fit_transform(dataset['soup'])
cosine_sim2 = cosine_similarity(matrix, matrix)
l=[]



#features = dataset['Genres']
#for feature in features:
    #dataset[feature] = dataset[feature].apply(literal_eval)
def find_title_from_index(index):
    return dataset[dataset.index == index]["aTitle"].values[0]
def get_recommendations(title, cosine_sim=cosine_sim2):
        if title not in dataset['aTitle'].unique():
            return "Not in Database"
        else:
            i=dataset.loc[dataset['aTitle']== title].index[0]
            lst = list(enumerate(cosine_sim2[i]))
            lst= sorted(lst,key=lambda x:x[1],reverse=True)[1:]
            i=0
            for element in lst:   
                print(find_title_from_index(element[0]))
                i=i+1
                if i>5:
                    break
            
            #for i in range(len(lst)):
                #a = lst[i][0]
                #l.append(dataset['aTitle'][a])
            #for i in range(len(l)):
                
                #return(l[i])

class Recommendation(Resource):
    

    
    
    def get(self):
        args = parser.parse_args()
        user_query = args['query']
        pred=[]
        
        pred = get_recommendations('Adore You')
        print(pred)
        output = {'prediction': pred, 'id:2': 2
        }
        return output



api.add_resource(Recommendation, '/','/x')


if __name__ == '__main__':
    app.run(debug=True)
