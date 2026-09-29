namn = input("Hej vad heter du?")

print("hej " + namn + " välkommen till uppdraget att handla åt mormor!")

destination = input("Vart vill du gå Ica eller Coop?")



if destination.lower() == "ica":
    print("Du går till Ica")

    print("När du kommer fram till Ica så finns det ett gäng med 7 klassare som vill att du ska köpa ut energidicka åt dom. Kommer du göra det eller inte?")

    viktigt_val = input("Ja eller Nej?")

    if viktigt_val.lower() == "ja":
        print("Duhandlar åt mormor och köper ut energidicka åt 7 klassarna tyvärr så blir du polisanmäld av Anna Karin och blir sen arresterad av snuten. Du förlorade spelet")
    elif viktigt_val.lower() == "nej":
        print("7 klassarna blir sura på dig de slår ner dig och rånar dig. Du förlorade")
    else:
        print("Välj Ja eller Nej")
        while True:
            viktigt_val = input("Ja eller Nej?")
            if viktigt_val.lower() == "ja":
                print("Duhandlar åt mormor och köper ut energidicka åt 7 klassarna tyvärr så blir du polisanmäld av Anna Karin och blir sen arresterad av snuten. Du förlorade spelet")
                break
            elif viktigt_val.lower() == "nej":
                print("7 klassarna blir sura på dig de slår ner dig och rånar dig. Du förlorade")
                break
            else:
                print("Välj Ja eller Nej")      
elif destination.lower() == "coop":
    print("Du går till Coop")

    print("När du kommer till Coop så finns det en lång kö med pensionärer som håller på att handla så du får antingen vänta i en kö jätte länge eller så får du ta snabbkassan.)")

    the_way = input("Tar du snabbkassan eller kön?")

    if the_way.lower() == "snabbkassan":
        print("Någon 7 klassare hade mixtrad med fel sladdarna i snabbkassan så den exploderade och du dog. Du förlorade spelet")
    elif the_way.lower() == "kön":
        print("Kön är så långsam så att pensionärerna börja dö av ålder men du kan klara vänt tiden för att du är så mycket yngre.")

        print("När du kommer ut ur Coop så ser du Final bossen Anna Karin hon är en Karen som vill att du ska dö. Du måste välja om du ska fly eller slåss mot henne.")

        anna_karin = input("fly eller slåss? ")
        if anna_karin.lower() == "fly":
            print("Du springer undan med mormors varor du överlever och din mormor blir glad att du handlade åt hon. Du vann grattis!")
        elif anna_karin.lower() == "slåss":
            print("Anna Karinlägger sig på marken och rullar runt och säger att du slog hon en polis i närheten ser detta och skjuter dig på stället för att du Anna Karin var så trovärdig. Du förlorade")
        else:
            print("Välj fly eller slåss")
            while True:
                anna_karin = input("fly eller slåss? ")
                if anna_karin.lower() == "fly":
                    print("Du springer undan med mormors varor du överlever och din mormor blir glad att du handlade åt hon. Du vann grattis!")
                    break
                elif anna_karin.lower() == "slåss":
                    print("Anna Karinlägger sig på marken och rullar runt och säger att du slog hon en polis i närheten ser detta och skjuter dig på stället för att du Anna Karin var så trovärdig. Du förlorade")
                    break
                else:
                    print("Välj fly eller slåss")       
else:
    print("Välj Ica eller Coop")
    while True:
        destination = input("Vart vill du gå Ica eller Coop?")
        if destination.lower() == "ica":
            print("Du går till Ica")
            break
        elif destination.lower() == "coop":
            print("Du går till Coop")
            break
        else:
            print("Välj Ica eller Coop")
