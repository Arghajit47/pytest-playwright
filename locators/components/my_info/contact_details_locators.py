class ContactDetailsLocators:
    CONTACT_DETAILS_INPUT_FIELDS = lambda fieldLabel : f"(//label[normalize-space(text())='{fieldLabel}']/following::input)[1]"
    CONTACT_DETAILS_DROPDOWN_FIELDS = "(//div[@class='oxd-select-text-input'])[1]" 