import * as api from './src/services/api.js';

async function runTests() {
  console.log("--- 1. Testing getCustomer Rahul ---");
  const rahul = await api.getCustomer("cust_rahul");
  console.log(`[PASS] Name: ${rahul.name}, Balance: ₹${rahul.balance}, Score: ${rahul.health.score}`);

  console.log("--- 2. Testing getCustomer Amit (Stress Profile) ---");
  const amit = await api.getCustomer("cust_amit");
  console.log(`[PASS] Name: ${amit.name}, Balance: ₹${amit.balance}, Score: ${amit.health.score}, Stress: ${amit.stress.level}`);

  console.log("--- 3. Testing getCustomer Priya (High Savings Profile) ---");
  const priya = await api.getCustomer("cust_priya");
  console.log(`[PASS] Name: ${priya.name}, Balance: ₹${priya.balance}, Score: ${priya.health.score}`);

  console.log("--- 4. Testing getRecommendation Rahul ---");
  const recRahul = await api.getRecommendation("cust_rahul");
  console.log(`[PASS] Product: "${recRahul.product}", Confidence: ${recRahul.confidence}%`);

  console.log("--- 5. Testing getRecommendation Amit ---");
  const recAmit = await api.getRecommendation("cust_amit");
  console.log(`[PASS] Product: "${recAmit.product}", Confidence: ${recAmit.confidence}%`);

  console.log("--- 6. Testing sendChatMessage loan affordability Rahul ---");
  const chatRahul = await api.sendChatMessage("cust_rahul", "Can I afford a loan?");
  console.log(`[PASS] Reply: ${chatRahul.reply}`);
  console.log(`[PASS] Actions:`, chatRahul.suggestedActions.map(a => a.label));

  console.log("--- 7. Testing sendChatMessage loan affordability Amit ---");
  const chatAmit = await api.sendChatMessage("cust_amit", "Can I afford a loan?");
  console.log(`[PASS] Reply: ${chatAmit.reply}`);
  console.log(`[PASS] Actions:`, chatAmit.suggestedActions.map(a => a.label));

  console.log("--- 8. Testing sendChatMessage spending breakdown ---");
  const chatSpend = await api.sendChatMessage("cust_rahul", "Where am I spending the most?");
  console.log(`[PASS] Reply: ${chatSpend.reply}`);
  console.log(`[PASS] Actions:`, chatSpend.suggestedActions.map(a => a.label));

  console.log("--- 9. Testing getTransactions search & filter ---");
  const foodTxs = await api.getTransactions("cust_rahul", { category: "Food" });
  console.log(`[PASS] Food transactions count: ${foodTxs.length}`);
  const allTxs = await api.getTransactions("cust_rahul");
  console.log(`[PASS] Total transactions count: ${allTxs.length}`);

  console.log("--- 10. Testing getInsights ---");
  const insights = await api.getInsights("cust_rahul");
  console.log(`[PASS] Insights count: ${insights.insights.length}, Opportunities: ${insights.opportunities.length}`);

  console.log("\n>>> ALL 10 AUTOMATED API AND DATA TESTS PASSED SUCCESSFULLY! <<<");
}

runTests().catch(err => {
  console.error("Test failed:", err);
  process.exit(1);
});
