class CreatedByUserRequiredException(Exception):

    def __str__(self):
        return 'Created by User is required'
