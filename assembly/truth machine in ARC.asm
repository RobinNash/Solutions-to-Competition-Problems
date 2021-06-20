! Truth Machine !
! By Robin Nash !
! User inputs a character. If 0 is inputted, 0 will be displayed
! to console and program will end.
! If 1 (or any character) is inputted, that character will be
! outputted infinitely.

   .begin
BASE .equ 0x3fffc0 ! Start of ports' memory locations
COUT .equ 0x0      ! Console Data Port
COSTAT .equ 0x4    ! Console Status Port
CIN .equ 0x8       ! Keyboard Data Port
CICTL .equ 0xc     ! Keyboard Control Port
	.org 2048
 	add %r0, %r0, %r4 ! Clear %r4
 	sethi BASE, %r4

In:
 	ld [%r4 + CICTL], %r1  ! load keyboard status to %r1
 	andcc %r1, 0x80, %r1   ! check if ready
 	be In                  ! if not ready, try again
 	ld [%r4 + CIN], %r3    ! put the character in %r3
 	subcc %r3, 48, %r6     ! store 1 or 0 in %r6 based on user input

Out: 
    ld [%r4 + COSTAT], %r1 ! load console status to %r1
 	andcc %r1, 0x80, %r1   ! check status
 	be Out                 ! if not ready, try again
 	st %r3, [%r4 + COUT]   ! print the inputted character
 	ba Loop

Loop: 
 	addcc %r0, %r6, %r0    ! check if inputted character is 0
 	be End                 ! if so, end the program
 	ba Out                 ! else, print it again
 

End: halt
 	.end
