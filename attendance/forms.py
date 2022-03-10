# class AttendanceForm(forms.ModelForm):
#     class Meta:
#         model = Attendance
#         exclude = ['date_added',
#                    'date_updated', 'is_deleted',]
#         widgets = {
#             'staff': Select(attrs={'class': 'required form-control select2'}),
#             'date': DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'id': 'Date', 'name': 'date', 'type': 'date'}),
#             'entry_time': TimeInput(attrs={'class': 'timepicker form-control ', 'type': 'time'}),
#             'exit_time': TimeInput(attrs={'class': 'timepicker form-control', 'type': 'time'}),
#             # 'fine_amount': TextInput(attrs={'class': ' form-control', 'placeholder': 'Enter fine amount'}),
#         }
#         labels = {
#         }
