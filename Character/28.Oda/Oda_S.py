import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 3)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "50 + 1n Tank", 75, 0);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 1)
         {
            f.SquareShape(cp, 1, "50 + 1n Tank", 125, 50);
            f.SquareShape(cp, 1, "50 + 1n Tank", 50, 125);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 3)
         {
            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 4, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Goliath", 45, 4, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 4, 75, 0);
            f.LineShape(cp, 1, "40 + 1n Goliath", 135, 4, 75, 0);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 75, 0);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 125, 50);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 50, 125);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 5)
         {
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