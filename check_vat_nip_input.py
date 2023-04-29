import check_vat_nip

def main():
    nip = input("Enter NIP: ")
    try:
        subject = check_vat_nip.check_vat_nip(nip)
        print("Subject found:")
        print(subject)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
