awk '{
    if ($2>=50 && $3>=50 && $4>=50) {
        pf = "Pass"
    }
    else {
        pf = "Fail"
    }
    { print $1 " : " pf }
}'

# awk '{
#     pf = ($2>=50 && $3>=50 && $4>=50) ? "Pass" : "Fail"
#     print $1 ":" pf
# }'