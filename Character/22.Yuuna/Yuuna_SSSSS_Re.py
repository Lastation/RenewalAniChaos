import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 3, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 5, 75);
            f.NxNSquareShape(cp, 1, "40 + 1n Goliath", 3, 50);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 5, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.NxNSquareShape(cp, 1, "Kakaru (Twilight)", 5, 75);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;


         }
         else if (f.loop[cp] == 1)
         {         
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 5, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

         
      }
      else if (f.count[cp] == 2)
      {
         f.SkillEnd(cp);
      }
   }
}