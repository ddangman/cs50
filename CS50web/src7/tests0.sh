python -c "from tests0 import test_prime; test_prime(1, False)"
python -c "from tests0 import test_prime; test_prime(2, True)"
python -c "from tests0 import test_prime; test_prime(8, False)"
python -c "from tests0 import test_prime; test_prime(11, True)"
python -c "from tests0 import test_prime; test_prime(25, False)"
python -c "from tests0 import test_prime; test_prime(28, False)"

python -c "from tests0 import test_prime; test_prime(101, True)"
python -c "from tests0 import test_prime; test_prime(101, False)" # should fail
# run in Bash
# $ ./tests0.sh