import test
import library



def main():
    user_input = library.receive_user_input()
    money_transcription = library.transcript_the_amount_of_money(user_input)
    print(f'надана вами сума: {money_transcription}')


if __name__ == "__main__":
    main()


