# import csv
# import datetime
# from itertools import islice
# from django.conf import settings
# from django.core.management.base import BaseCommand
# from core.models import NetflixMovie

# class Command(BaseCommand):
#     help = 'Load data from ViewingActivity file'

#     def handle(self, *args, **kwargs):
#         datafile = settings.BASE_DIR / 'data' / 'ViewingActivity.csv'

#         one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)

#         with open(datafile, 'r', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(islice(csvfile, 0, 4952))
#             # Profile Name,Start Time,Duration,Attributes,Title,Supplemental Video Type,Device Type,Bookmark,Latest Bookmark,Country
#             for row in reader:
#                 profile_name = row['Profile Name']
#                 start_time = datetime.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')

#                 dur_hours, dur_minutes, dur_seconds = map(int, row['Duration'].split(':'))
#                 duration = datetime.timedelta(hours=dur_hours, minutes=dur_minutes, seconds=dur_seconds)

#                 attributes = row['Attributes']
#                 title = row['Title']
#                 supplemental_video_type = row['Supplemental Video Type']
#                 device_type = row['Device Type']

#                 book_hours, book_minutes, book_seconds = map(int, row['Bookmark'].split(':'))
#                 bookmark = datetime.timedelta(hours=book_hours, minutes=book_minutes, seconds=book_seconds)

#                 # Catch 'Not latest View' exception
#                 latest_bookmark = datetime.timedelta(days=-1)
#                 if row['Latest Bookmark'] != 'Not latest view':
#                     latest_hours, latest_minutes, latest_seconds = map(int, row['Latest Bookmark'].split(':'))
#                     latest_bookmark = datetime.timedelta(hours=latest_hours, minutes=latest_minutes, seconds=latest_seconds)

#                 country = row['Country']

#                 # Create and save NetflixMovie object
#                 NetflixMovie.objects.create(
#                     profile_name=profile_name,
#                     start_time=start_time,
#                     duration=duration,
#                     attributes=attributes,
#                     title=title,
#                     supplemental_video_type=supplemental_video_type,
#                     device_type=device_type,
#                     bookmark=bookmark,
#                     latest_bookmark=latest_bookmark,
#                     country=country
#                 )



import csv
import datetime
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import NetflixMovie

class Command(BaseCommand):
    help = 'Load data from ViewingActivity file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'ViewingActivity.csv'

        one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
        NetflixMovie.objects.filter(start_time__lt=one_year_ago).delete()

        with open(datafile, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                start_time = datetime.datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')

                # Check if the start time is within the last year
                if start_time >= one_year_ago:
                    profile_name = row['Profile Name']

                    dur_hours, dur_minutes, dur_seconds = map(int, row['Duration'].split(':'))
                    duration = datetime.timedelta(hours=dur_hours, minutes=dur_minutes, seconds=dur_seconds)

                    attributes = row['Attributes']
                    title = row['Title']
                    supplemental_video_type = row['Supplemental Video Type']
                    device_type = row['Device Type']

                    book_hours, book_minutes, book_seconds = map(int, row['Bookmark'].split(':'))
                    bookmark = datetime.timedelta(hours=book_hours, minutes=book_minutes, seconds=book_seconds)

                    # Catch 'Not latest View' exception
                    latest_bookmark = datetime.timedelta(days=-1)
                    if row['Latest Bookmark'] != 'Not latest view':
                        latest_hours, latest_minutes, latest_seconds = map(int, row['Latest Bookmark'].split(':'))
                        latest_bookmark = datetime.timedelta(hours=latest_hours, minutes=latest_minutes, seconds=latest_seconds)

                    country = row['Country']

                    # Create and save NetflixMovie object
                    NetflixMovie.objects.create(
                        profile_name=profile_name,
                        start_time=start_time,
                        duration=duration,
                        attributes=attributes,
                        title=title,
                        supplemental_video_type=supplemental_video_type,
                        device_type=device_type,
                        bookmark=bookmark,
                        latest_bookmark=latest_bookmark,
                        country=country
                    )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
