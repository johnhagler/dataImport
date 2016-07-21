import utils


class CvxCode(object):

    def __init__(self, line):

        self.code = line[0].strip()
        self.short_description = line[1].strip()
        self.full_vaccine_name = line[2].strip()
        self.notes = line[3].strip()
        self.status = line[4].strip()
        self.non_vaccine = line[5].strip()
        self.update_date = utils.convert_date_format(line[6], '%Y/%m/%d', '%Y-%m-%d')

    def get_values(self):
        return self.code, self.short_description, self.full_vaccine_name, \
               self.notes, self.status, self.non_vaccine,  self.update_date
