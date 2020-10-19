import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         if (f.loop[cp] < 5)
         {
            f.DoubleShape(cp, 1, "Protoss Dark Archon", -100, 100 - 50 * f.loop[cp]);            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            f.DoubleShape(cp, 1, "40 + 1n Goliath", 100 - 50 * f.loop[cp], 100);            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);         
         }
         if (f.loop[cp] == 5)
         {
            f.DoubleShape(cp, 1, "Protoss Dark Archon", -50, 100);    
            f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 50);            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]); 
         }
         if (f.loop[cp] == 6)
         {
            f.DoubleShape(cp, 1, "Protoss Dark Archon", 0, -100); 
            f.DoubleShape(cp, 1, "40 + 1n Goliath", -100, 0);            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]); 
         }
         if (f.loop[cp] == 7)
         {
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45,3, 50); 
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45,3, 50);            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);       
         }
          f.SkillWait(cp, 80);

          f.loop[cp] += 1;

          if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0; 
         }
      }
       
      else if (f.count[cp] == 1)
      {
          KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
          KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}