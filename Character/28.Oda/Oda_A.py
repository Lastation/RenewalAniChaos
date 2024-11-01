import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

         f.Table_Sin(cp, 22 + 45 * f.loop[cp], 100);
         f.Table_Cos(cp, 22 + 45 * f.loop[cp], 100);

         f.SquareShape(cp, 1, "Rhynadon (Badlands)", f.CosAngle[cp], f.SinAngle[cp]);
         KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

         f.DotShape(cp, 1, "40 + 1n Wraith", 0, 0);
         Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");

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
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.EdgeShape(cp, 1, "50 + 1n Tank", 45, 5, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         else if (f.loop[cp] == 1)
         {
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 100);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 3, 50);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
         }
         else if (f.loop[cp] == 3)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }
         else if (f.loop[cp] == 4)
         {
            f.LineShapeAt(cp, 1, "40 + 1n Wraith", 135, 4, 50, 100, 50);
            f.LineShapeAt(cp, 1, "40 + 1n Wraith", 135, 4, 50, -100, -50);
            f.LineShapeAt(cp, 1, "50 + 1n Tank", 135, 4, 50, 100, 50);
            f.LineShapeAt(cp, 1, "50 + 1n Tank", 135, 4, 50, -100, -50);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 5)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShapeAt(cp, 1, "40 + 1n Wraith", 45, 4, 50, -50, 100);
            f.LineShapeAt(cp, 1, "40 + 1n Wraith", 45, 4, 50, 50, -100);
            f.LineShapeAt(cp, 1, "50 + 1n Tank", 45, 4, 50, -50, 100);
            f.LineShapeAt(cp, 1, "50 + 1n Tank", 45, 4, 50, 50, -100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         }

         f.SkillWait(cp, 160);

         f.loop[cp] += 1;

         if (f.loop[cp] == 7)
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