__author__ = 'perecullera'

csv_filepathname = "allotjament.csv"

import csv, sys, os
import django

from django.conf import settings
from tourapp.models import Category, Apartment

sys.path.append("/Users/perecullera/virtualen/django_tour_proj/django_tour_proj")
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_tour_proj.settings'

settings.configure()

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

category_list = list(Category.objects.all())
print "category_list: " + str(category_list)
for row in dataReader:
    if row[0] == "id":
        print row;
    else:
        print "Catrow= " + str(row)
        cat = row[9]
        if cat not in category_list:
            print "Cat= " + cat
            category_list.append(cat)
            category = Category()
            category.name = cat
            category.save()

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
fields = ['id_2', 'latitude', 'longitude', 'address', 'created', 'district', 'name', 'neighborhood', 'postal_code',
          'cats']
for row in dataReader:
    #treiem la primera linia
    if row[0] == "id":
        print row;
    else:
        #comprovem si l'hotel ja hi és
        if Apartment.objects.get(name=row[6]):
            print "aptrow " + str(row)
            cat = Category.objects.get(name=row[9])
            row[9] = cat
            row[0] = int(row[0])
            row[1] = float(row[1])
            row[2] = float(row[2])
            if row[8]=='None':
                row[8] = 0
            else:
                #we need to put an extra 0 on postal_code
                row[8] = int(0+row[8])

            Apartment.objects.create(**dict(zip(fields, row)))

        else :
            Apartment.objects.get(name=row[6]).cats.add(row[9]).save()



