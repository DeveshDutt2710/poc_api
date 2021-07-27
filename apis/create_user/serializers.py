# import json
# from bson import json_util
# from collections import OrderedDict  # don't remove this import
# from rest_framework import serializers
# from .models import Profiles, Address, Contact, PrivacySettings


# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     """
#     A ModelSerializer that takes an additional `fields` argument that
#     controls which fields should be displayed.
#     """

#     def __init__(self, *args, **kwargs):
#         # Don't pass the 'fields' arg up to the superclass
#         fields = kwargs.pop('fields', None)

#         # Instantiate the superclass normally
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

#         if fields is not None:
#             # Drop any fields that are not specified in the `fields` argument.
#             allowed = set(fields)
#             existing = set(self.fields)
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)





# class NearestCitySerializer(DynamicFieldsModelSerializer):
#     profile_contacts = ContactSerializer(many=True,read_only=True, source='contact_set')

#     class Meta:
#         model = Profiles
#         fields = ['id','name','profile_contacts','profile_type','vendor_description','privacy_setting','dob','gender','image','last_app_activity','created_at','updated_at','is_deleted','is_admin_verified',]
#         depth = 2
