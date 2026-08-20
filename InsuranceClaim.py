from datetime import datetime


class InsuranceClaim:

    def __init__(self):
        self.claims = []

    def process_claim(self, policy_number, customer_id,
                      policy_type, claim_amount,
                      policy_start_date, incident_date,
                      previous_claim_count, customer_age,
                      incident_type, documents_available):

        start = datetime.strptime(policy_start_date, "%Y-%m-%d")
        incident = datetime.strptime(incident_date, "%Y-%m-%d")

        if not policy_number:
            print("Invalid policy number")
            return

        if incident < start:
            print("Claim before policy start")
            return

        coverage = {
            "Health": 100000,
            "Vehicle": 200000,
            "Life": 500000
        }

        if policy_type not in coverage:
            print("Invalid policy type")
            return

        maximum_payable = coverage[policy_type]

        deductible = maximum_payable * 0.10

        fraud_score = 0

        # Multiple previous claims
        if previous_claim_count >= 3:
            fraud_score += 25

        # Claim amount significantly higher than coverage
        if claim_amount > maximum_payable:
            fraud_score += 30

        # Incident immediately after policy activation
        days_after_activation = (incident - start).days

        if days_after_activation <= 7:
            fraud_score += 25

        # Missing documents
        if not documents_available:
            fraud_score += 20

        # Customer age validation
        if customer_age < 18:
            print("Invalid customer age")
            return

        # Eligibility
        if claim_amount <= 0:
            print("Invalid claim amount")
            return

        if claim_amount > maximum_payable:
            eligibility = False
        else:
            eligibility = True

        if fraud_score >= 70:
            classification = "FRAUD SUSPECTED"

        elif not documents_available:
            classification = "MANUAL REVIEW"

        elif not eligibility:
            classification = "REJECTED"

        else:
            classification = "APPROVED"

        if eligibility:
            payable = min(claim_amount, maximum_payable)
            payout = max(0, payable - deductible)
            customer_contribution = deductible
        else:
            payout = 0
            customer_contribution = 0

        print("Claim eligibility:", eligibility)
        print("Maximum payable:", maximum_payable)
        print("Deductible:", deductible)
        print("Customer contribution:", customer_contribution)
        print("Insurance payout:", payout)
        print("Fraud risk score:", fraud_score)
        print("Classification:", classification)

        self.claims.append({
            "policy": policy_number,
            "customer": customer_id,
            "amount": claim_amount,
            "classification": classification
        })


insurance = InsuranceClaim()

insurance.process_claim(
    "POL1001",
    "CUS001",
    "Health",
    50000,
    "2025-01-01",
    "2026-01-01",
    0,
    30,
    "Medical",
    True
)
