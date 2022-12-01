readed_file = open("doctors_aid_inputs.txt", "r", encoding="utf8").read().replace(',', '').split("\n")
output = open("doctors_aid_outputs.txt", "w", encoding="utf8")

patient_raw = list()
patient_processed = list()


def patientCreator(patient_array):
    if not patient_array[0] in patient_raw:
        patient_raw.append(patient_array)
        current_patient = [patient_array[0], patient_array[2]]
        current_patient += probabilityCalculator(patient_array)
        patient_processed.append(current_patient)
        output.write("Patient {} is recorded.\n".format(patient_array[0]))
    elif patient_array in patient_raw:
        output.write("Patient {} cannot be recorded due to duplication.\n".format(patient_array[0]))


def patientRemover(patient_name):
    for patient in patient_raw:
        if patient[0] == patient_name:
            patient_raw.remove(patient)
            output.write("Patient {} is removed.\n".format(patient_name))
            for patient in patient_processed:
                if patient[0] == patient_name:
                    patient_processed.remove(patient)
                    break
            break


def patientRecommendation(patient_name):
    for patient in patient_processed:
        if patient[0] == patient_name:
            if patient[3] > patient[2]:
                output.write("System suggests {} NOT to have the treatment.\n".format(patient[0]))
                break
            else:
                output.write("System suggests {} to have the treatment.\n".format(patient[0]))
                break


def patientLister():
    namelen = max(len(patient[0]) for patient in patient_raw) + 1
    diseaselen = max(len(patient[2]) for patient in patient_raw) + 8
    treatmentlen = 13
    totallen = namelen + diseaselen + treatmentlen + 10 + 10 + 10
    treatment = "Not Assigned"
    table_head_1 = ['Patient', 'Diagnosis', 'Disease', 'Disease', 'Treatment', 'Treatment']
    table_head_2 = ['Name', 'Accuracy', 'Name', 'Incidence', 'Name', 'Risk']

    output.write(
        f"{table_head_1[0].ljust(namelen)}{table_head_1[1].ljust(10)}{table_head_1[2].ljust(diseaselen)}{table_head_1[3].ljust(10)}{table_head_1[4].ljust(treatmentlen)}{table_head_1[5].ljust(10)}\n")
    output.write(
        f"{table_head_2[0].ljust(namelen)}{table_head_2[1].ljust(10)}{table_head_2[2].ljust(diseaselen)}{table_head_2[3].ljust(10)}{table_head_2[4].ljust(treatmentlen)}{table_head_2[5].ljust(10)}\n")
    output.write("-" * (totallen - 1) + "\n")
    for patient in patient_raw:
        diseasename = patient[2] + " Cancer"
        accuracy = f"{round(float(patient[1])*100, 2):.2f}%"
        risk = f"{round(float(patient[-1])*100,2):.2f}%"
        output.write(
            f"{patient[0].ljust(namelen)}{accuracy.ljust(10)}{diseasename.ljust(diseaselen)}{patient[3].ljust(10)}{treatment.ljust(treatmentlen)}{risk.ljust(10)}\n"
        )


def probabilityCalculator(patient):
    test_accuracy = float(patient[1])
    num, denom = patient[3].split('/')
    cancer_rate = float(num) / float(denom)
    population = 1
    nominator = population * cancer_rate * test_accuracy
    denominator = nominator + (1 - test_accuracy) * (population - population * cancer_rate)
    calculated_value = [nominator / denominator, float(patient[-1])]
    return calculated_value


def patientProbability(patient_name, isInput):
    if isInput:
        is_printed = False
        for j in patient_processed:
            if j[0] == patient_name:
                output.write("Patient {} has a probability of {} of having {} cancer.\n".format(patient_name,
                                                                                                str(round(j[2] * 100,
                                                                                                          2)) + "%",
                                                                                                j[1].lower()))

                is_printed = True
                break
        if not is_printed:
            output.write("Probability for {} cannot be calculated due to absence.\n".format(line[1]))
    else:
        return round(patient_name * 100, 2)


for line in readed_file:
    line = line.split()
    if line[0] == 'create':
        del line[0]
        del line[3]
        patientCreator(line)
    elif line[0] == 'remove':
        patientRemover(line[1])
    elif line[0] == 'recommendation':
        patientRecommendation(line[1])
    elif line[0] == 'probability':
        patientProbability(line[1], True)
    elif line[0] == 'list':
        patientLister()
