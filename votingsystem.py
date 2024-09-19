nominee1 = input("Enter the Name of First Nominee : ")
nominee2 = input("Enter the Name of Second Nominee : ")
nominee3 = input("Enter the Name of Third Nominee : ")
nominee4 = input("Enter the Name of Third Nominee : ")

nm1_votes = 0
nm2_votes = 0
nm3_votes = 0
nm4_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]
no_of_voter = len(voter_id)

while True:
    if voter_id  ==[]:
        print("Voting session is over!")
        percent = (nm1_votes/no_of_voter*100)
        if nm1_votes > nm2_votes and nm1_votes > nm3_votes and nm1_votes > nm4_votes:
            print(nominee1, "has won the election with", percent, "% votes.")
            break
        elif nm2_votes > nm1_votes and nm2_votes > nm3_votes and nm2_votes > nm4_votes:
            print(nominee2, "has won the election with", percent, "% votes.")
            break
        elif nm3_votes > nm1_votes and nm3_votes > nm2_votes and nm3_votes > nm4_votes:
            print(nominee3, "has won the election with", percent, "% votes.")
            break
        elif nm4_votes > nm1_votes and nm4_votes > nm2_votes and nm4_votes > nm3_votes:
            print(nominee4, "has won the election with", percent, "% votes.")
            break
        else:
            print("Both have equal number of votes!")
            break



    voter = int(input("Enter your Voterid: "))
    if voter in voter_id:
        print("Voter Authentication is successfull!  ")
        voter_id.remove(voter)

        print("===========================================================")

        print("To give vote to ",nominee1, "Press 1 ")
        print("To give vote to ",nominee2, "Press 2 ")
        print("To give vote to ",nominee3, "Press 3 ")
        print("To give vote to ",nominee4, "Press 4 ")

        print("===========================================================")

        vote = int(input("Enter your precious Vote : "))

        if vote == 1:
            nm1_votes +=1
            print(nominee1,"Thank you very much for Voting!")
        elif vote == 2:
            nm2_votes +=1
            print(nominee2,"Thank you very much for Voting!")
        elif vote == 3:
            nm3_votes +=1
            print(nominee3,"Thank you very much for Voting!")
        elif vote == 4:
            nm4_votes +=1
            print(nominee4,"Thank you very much for Voting!")
        elif vote > 4 or vote==0:
            print("Please Check the pressed key again, you can input only 1,2,3 and 4. ")
        else:
            print("Failed to input your vote")
        


    