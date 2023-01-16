function indexMatchingText(options, hour) {
    // Return the exact index of the hour I need to remove from options
    for (let i = 0; i < options.length; i++) {
        if (options[i].childNodes[0].nodeValue === hour) {
            return i;
        }
    }
    return undefined;
}

function resetOptions(selectElement, new_options) {
    // Clears all the options
    let i, L = selectElement.options.length - 1;
    for (i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
    // Builds a new full option list
    for (let i = 0; i < new_options.length; i++) {
        let hour = new_options[i];
        let option = document.createElement("option")
        option.textContent = hour;
        option.value = `${i}`;
        selectElement.appendChild(option);
    }
}

function showhours() {
    // sets the hour options with the filtering via the given date.
    let year = document.getElementById('id_appointment_date_year')
    let month = document.getElementById('id_appointment_date_month')
    let month_value = month.value
    if (Number(month.value) < 10) {
        month_value = `0${month.value}`
    }
    let day = document.getElementById('id_appointment_date_day')
    let chosen_date = `${year.value}-${month_value}-${day.value}`
    let available_hours = document.getElementById('id_hour_slot')
    resetOptions(available_hours, business_hours)
    for (let x of dates) {
        if (x["date"] === chosen_date) {
            if (business_hours[x["slot"]] === x["hour"]) {
                available_hours.options[indexMatchingText(available_hours, x["hour"])].remove()
            }
        }
    }
}


