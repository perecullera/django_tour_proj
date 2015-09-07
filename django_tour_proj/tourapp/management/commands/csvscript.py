import csv
from tourapp.models import Category, Apartment

__author__ = 'perecullera'

from django.core.management.base import BaseCommand, CommandError

csv_filepathname = "allotjament.csv"


class Command(BaseCommand):

    def handle(self,*args,**options):
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
        fields = ['id_2', 'latitude', 'longitude', 'address', 'created', 'district', 'name', 'neighborhood', 'postal_code']
        for row in dataReader:
            #treiem la primera linia
            if row[0] == "id":
                print row;
            else:
                #comprovem si l'hotel ja hi es
                if not Apartment.objects.filter(id_2=row[0]).exists():
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
                        row[8] = 0+int(row[8])

                    apt = Apartment.objects.create(**dict(zip(fields, row)))
                    apt.cats.add(row[9])
                    print "Apartment added" + apt.name

                else :
                    apt = Apartment.objects.get(id_2=row[0])
                    print apt
                    cat = Category.objects.get(name=row[9])
                    apt.cats.add(cat)
                    apt.save()
                    print "Apartment added " + str(apt)

