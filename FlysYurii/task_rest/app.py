from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

websites = [
    {
        'id': 1,
        'title': 'Google',
        'description': 'Search engine'
    },
    {
        'id': 2,
        'title': 'Facebook',
        'description': 'Social network'
    },
    {
        'id': 3,
        'title': 'Youtube',
        'description': 'Video hosting'
    },
    {
        'id': 4,
        'title': 'Amazon',
        'description': 'Online store'
    }
]


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')


class WebsiteList(Resource):
    def get(self):
        return websites

    def post(self):
        args = parser.parse_args()
        website = {'id': websites[-1]['id'] + 1, 'title': args['title'], 'description': args['description']}
        websites.append(website)
        return website, 201


class Website(Resource):
    def get(self, website_id):
        website = next((website for website in websites if website['id'] == website_id), None)
        if website:
            return website
        return {'message': 'Website not found'}, 404

    def patch(self, website_id):
        args = parser.parse_args()
        website = next((website for website in websites if website['id'] == website_id), None)
        if website:
            for key, value in args.items():
                if value is not None:
                    website[key] = value
            return website
        return {'message': 'Website not found'}, 404

    def delete(self, website_id):
        global websites
        websites = [website for website in websites if website['id'] != website_id]
        return {'message': 'Website deleted'}


api.add_resource(WebsiteList, '/websites')
api.add_resource(Website, '/websites/<int:website_id>')

if __name__ == "__main__":
    app.run(debug=True)
