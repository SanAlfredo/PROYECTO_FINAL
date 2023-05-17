import datetime


class DateFormat():

    @classmethod
    def convertir_fecha(self, fecha):
        return datetime.datetime.strftime(fecha, '%d/%m/%Y')
