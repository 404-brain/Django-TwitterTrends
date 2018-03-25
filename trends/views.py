from django.shortcuts import render, HttpResponse
from django.http import Http404
from django.template import loader, Template, RequestContext
import twitter


# Create your views here.

# API KEYS
api = twitter.Api(
        consumer_key='SCwzwLqZ7bQd8AXB4IYByldOy',
        consumer_secret='U7J4jbFgJJVGJ13FIdM0QCVPyMbIPgkUJEocLFh9Fq6HLFBUwL',
        access_token_key='790034353-RWl8UKCt29u8hzpw639A02H1sotx1lhUlOBEkHLS',
        access_token_secret='0b4v5RuFUxvpC8yvfB99B6x8OXB0Zf5DzlJME9UGNkWd2'
    )


def home(request):

    trends = api.GetTrendsCurrent(exclude=None)
    searches = api.GetSearch(term='moments', raw_query=None, geocode=None, since_id=None,
                             max_id=None, until=None, since=None, count=30,
                             lang=None, locale=None, result_type="popular", include_entities=None)

    return render(request, 'trends/home.html', {'trends': trends, 'searches': searches})


def get_global_trends(request):

    ''' Gets current trends globally '''


    countries = {'Algeria':23424740,'Argentina':23424747,'Australia':23424748,'Austria':23424750,'Belarus':23424765,
               'Belgium':23424757,'Brazil':23424768,'Canada':23424775,'Chile':23424782,'Colombia':23424787,'Dominican Republic':23424800,
               'Ecuador':23424801,'Egypt':23424802,'France':23424819,'Germany':23424829,'Ghana':23424824,'Greece':23424833,'Guatemala':23424834,
               'India':23424848,'Indonesia':23424846,'Ireland':23424803,'Israel':23424852,'Italy':23424853,'Japan':23424856,
               'Jordan':23424860,'Kenya':23424863,'Korea':23424868,'Kuwait':23424870,'Latvia':23424874,'Lebanon':23424873,
               'Malaysia':23424901,'Mexico':23424900,'Netherlands':23424909,'New Zealand':23424916,'Nigeria':23424908,'Norway':23424910,
               'Oman':23424898,'Pakistan':23424922,'Panama':23424924,'Peru':23424919,'Philippines':23424934,'Poland':23424923,
               'Portugal':23424925,'Puerto Rico':23424935,'Qatar':23424930,'Russia':23424936,'Saudi Arabia':23424938,'Singapore':23424948,
               'South Africa':23424942,'Spain':23424950,'Sweden':23424954,'Switzerland':23424957,'Thailand':23424960,'Turkey':23424969,
               'Ukraine':23424976,'United Arab Emirates':23424738,'United Kingdom':23424975,'United States':23424977,
               'Venezuela':23424982,'Vietnam':23424984}

    trends = api.GetTrendsCurrent(exclude=None)

    return render(request, 'trends/tt.html', {'trends': trends,
                                              'countries': countries})

def country(request, name, id):

    woid_trends = api.GetTrendsWoeid(woeid=id, exclude=None)
    return render(request, 'trends/country/country.html', {'country': woid_trends, 'name': name})


def search(request):

    ''' Searches Hash & Users Related '''

    if request.method == "POST":
        user_search = request.POST.get('user-search')

        try:
            tweets_about = api.GetSearch(term=user_search, raw_query=None, geocode=None, since_id=None,
                                         max_id=None, until=None, since=None, count=16,
                                         lang=None, locale=None, result_type="latest", include_entities=None)
            if '#' in user_search:
                return render(request, 'trends/search/hash-search.html', {'user_search': user_search,
                                                                        'tweets_about': tweets_about})
            elif not '#' in user_search:
                user_sug = api.GetUsersSearch(term=user_search, page=1, count=16, include_entities=None)
                for users in user_sug:
                    return render(request, 'trends/search/no-hash-search.html', {'user_search': user_search,
                                                                             'user_sug': users,
                                                                             'tweets_about': tweets_about})
        except Exception:
            error_message = 'Invalid input or user is private....'
            return render(request, 'trends/search.html', {'error': error_message})

    return render(request, 'trends/search.html',)


def hash(request, hash_name):

    tweets = api.GetSearch(term=hash_name, raw_query=None, geocode=None, since_id=None,
                                 max_id=None, until=None, since=None, count=30,
                                 lang=None, locale=None, result_type="latest", include_entities=None)
    if '#' not in hash_name:
        return render(request, 'trends/hashtag/no-hash.html', {'hash': hash_name, 'tweets_about': tweets})
    return render(request, 'trends/hashtag/hash.html', {'hash': hash_name, 'tweets_about': tweets})


def user(request, user_name):

    timeline = api.GetUserTimeline(user_id=None, screen_name=user_name, since_id=None,
                                   max_id=None, count=None, include_rts=True, trim_user=False,
                                   exclude_replies=True)
    return render(request, 'trends/user/users.html', {"user": user_name, 'user_timeline': timeline})




