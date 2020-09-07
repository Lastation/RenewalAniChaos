import Function as f;

const s = StringBuffer();

function Shape(cp : TrgPlayer, x, y);

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0) Shape(cp, 50, 50);
         else if (f.loop[cp] == 1) Shape(cp, 0, 50);
         else if (f.loop[cp] == 2) Shape(cp, -50, 50);
         else if (f.loop[cp] == 3) Shape(cp, -50, 0);


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
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 0, 3, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 480);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 45, 5, 100);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            f.EdgeShape(cp, 1, "40 + 1n Goliath", 45, 5, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Gantrithor", 45, 7, 150);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 45, 7, 150);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 5, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);
            
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }
}

function Shape(cp : TrgPlayer, x, y)
{
   KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);
   f.DotShape(cp, 1, "Protoss Dark Templar", x, y);
   f.DotShape(cp, 1, "Protoss Dark Templar", -x, -y);
   f.DotShape(cp, 1, "40 + 1n Mojo", x, y);
   f.DotShape(cp, 1, "40 + 1n Mojo", -x, -y);
   f.DotShape(cp, 1, "Kakaru (Twilight)", -y, x);
   f.DotShape(cp, 1, "Kakaru (Twilight)", y, -x);
   f.DotShape(cp, 1, " Creep. Dunkelheit", -y, x);
   f.DotShape(cp, 1, " Creep. Dunkelheit", y, -x);
   KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
   KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);
   KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
   MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
   Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);
}