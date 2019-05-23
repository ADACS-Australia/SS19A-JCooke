"""
Distributed under the MIT License. See LICENSE.txt for more info.
"""

# Templates for different emails
VERIFY_EMAIL_ADDRESS = dict()
VERIFY_EMAIL_ADDRESS['subject'] = '[DWF] Please verify your email address'
VERIFY_EMAIL_ADDRESS['message'] = '<p>Dear {{first_name}} {{last_name}}: </p>' \
                                  '<p>We have received a new account request with our DWF system from this ' \
                                  'email address. Please verify your email address by clicking on the following ' \
                                  '<a href="{{link}}" target="_blank">link</a>: </p>' \
                                  '<p><a href="{{link}}" target="_blank">{{link}}</a> </p>' \
                                  '<p>If you believe that the email has been sent by mistake or you have not ' \
                                  'requested for an account please <strong>do not</strong> click on the link. </p>' \
                                  '<p>Alternatively you can report this incident to <a ' \
                                  'href="mailto:jcooke@astro.swin.edu.au" target="_top">jcooke@astro.swin.edu.au</a> ' \
                                  'for investigation. </p>' \
                                  '<p> </p>' \
                                  '<p>Regards, </p>' \
                                  '<p>DWF Team</p>'

ROLE_CHANGE_REQUEST = dict()
ROLE_CHANGE_REQUEST['subject'] = '[Action Required - DWF] Role Change Request'
ROLE_CHANGE_REQUEST['message'] = '<p>Dear Core Member: </p>' \
                                 '<p>We have received a role change request from this user: </p> ' \
                                 '<p>First Name: {{first_name}} </br>' \
                                 'Last Name: {{last_name}} </br>' \
                                 'Username: {{username}} </br>' \
                                 'Email: {{email}} </br>' \
                                 'Current Role: {{current_role}} </br>' \
                                 'Intended Role: {{intended_role}} </p>' \
                                 '<p>To action this request please click on the following ' \
                                 '<a href="{{link}}" target="_blank">link</a>: </p>' \
                                 '<p><a href="{{link}}" target="_blank">{{link}}</a> </p>' \
                                 '<p>If you believe that the email has been sent by mistake please ' \
                                 '<strong>do not</strong> click on the link. </p>' \
                                 '<p>Alternatively you can report this incident to <a ' \
                                 'href="mailto:jcooke@astro.swin.edu.au" target="_top">jcooke@astro.swin.edu.au</a> ' \
                                 'for investigation. </p>' \
                                 '<p> </p>' \
                                 '<p>Regards, </p>' \
                                 '<p>DWF Team</p>'
