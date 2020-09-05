import os
import easypost
# test tracking codes:
# https://www.easypost.com/docs/api#test-tracking-codes
# testing codes
# EZ1000000001 pre_transit
# EZ2000000002 in_transit
# EZ3000000003 out_for_delivery
# EZ4000000004 delivered
# EZ5000000005 return_to_sender
# EZ6000000006 failure
# EZ7000000007 unknown

easypost.api_key = os.environ.get('EASYPOST_API_KEY')

# delivery tracker
tracker = easypost.Tracker.create(
    tracking_code="EZ4000000004",
    carrier="USPS"
)

print(tracker)
