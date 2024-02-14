import django_tables2 as tables
from .models import Station
from jalali_date import date2jalali



class RecentRainGaugeTable(tables.Table):
    city = tables.Column(verbose_name='شهرستان', attrs={'th': {'class': 'text-center font-weight-bold'}, 'td': {'class': 'text-center font-weight-bold'}}, orderable=True)
    title = tables.Column(verbose_name='نام ایستگاه', attrs={'th': {'class': 'text-center font-weight-bold'}, 'td': {'class': 'text-center font-weight-bold'}}, orderable=True)
    recent_rainfall = tables.Column(verbose_name='بارندگی اخیر', attrs={'th': {'class': 'text-center font-weight-bold'}, 'td': {'class': 'text-center font-weight-bold'}}, orderable=True)
    last_rainfall_date_time = tables.Column(verbose_name='تاریخ و ساعت ثبت بارش',  attrs={'th': {'class': 'text-center font-weight-bold'}, 'td': {'class': 'text-center font-weight-bold'}}, orderable=True)

    def render_last_rainfall_date_time(self, value):
        if value is None:
            return ''
        else:
            jalali_date = date2jalali(value)
            return f"{value.hour}:{value.minute} -- {jalali_date.year}/{jalali_date.month}/{jalali_date.day}"


    class Meta:
        model = Station
        template_name = 'django_tables2/bootstrap4.html'
        fields = ['city', 'title', 'recent_rainfall','last_rainfall_date_time']
        attrs = {'class': 'table table-striped table-hover table-bordered table-sm'}

