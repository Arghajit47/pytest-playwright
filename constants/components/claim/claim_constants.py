from enum import Enum

class ClaimConstants:
    CLAIM_TAB_TEXT = "Claim"
    ASSIGN_CLAIM_TAB_TEXT = "Assign Claim"
    CLAIM_CREATE_SUCCESS_MESSAGE = "Successfully Saved"
    TEST_REMARKS = "Business travel expenses"
    CLAIM_DETAILS_URL_PATTERN = r".*/claim/assignClaim/id/\d+"
    TEST_EMPLOYEE_NAME = "Peter Mac Anderson"



class ClaimEvent(Enum):
    TRAVEL_ALLOWANCE = "Travel Allowance"
    ACCOMMODATION = "Accommodation"
    MEAL_ALLOWANCE = "Meal Allowance"

class ClaimCurrency(Enum):
    AFGHANISTAN_AFGHANI = "Afghanistan Afghani"
    EURO = "Euro"
    US_DOLLAR = "US Dollar"

class Api_Endpoints(Enum):
    CLAIM_ENDPOINT = "**/api/v2/claim/employees/*/requests"


